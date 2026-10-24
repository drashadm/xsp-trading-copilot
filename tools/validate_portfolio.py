"""Offline checks for this portfolio's Markdown, JSON and canonical diagram."""

import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


def anchors(text):
    result, counts = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        slug = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(f"{slug}-{count}" if count else slug)
    return result


def validate():
    failures, link_count = [], 0
    markdown = sorted(ROOT.rglob("*.md"))
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for target in re.findall(r"!?\[[^\]\n]*\]\(([^)\s]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme in ("https", "http", "mailto"):
                continue  # Offline by design; external availability is not checked.
            link_count += 1
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if parsed.scheme or not destination.is_relative_to(ROOT) or not destination.exists():
                failures.append(f"{path.relative_to(ROOT)}: invalid local target {target}")
            elif parsed.fragment and destination.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    failures.append(f"{path.relative_to(ROOT)}: missing anchor {target}")

    json_files = sorted((ROOT / "examples").glob("*.json"))
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as error:
            failures.append(f"{path.relative_to(ROOT)}: {error}")

    recommendation = json.loads((ROOT / "examples/sample_automatic_contract_recommendation.json")
                                .read_text(encoding="utf-8"))
    decision = recommendation.get("decision_support", {})
    if ("execution_payload" in recommendation or decision.get("execution_enabled") is not False
            or decision.get("approval_status") != "NOT_APPLICABLE_EXECUTION_DISABLED"
            or decision.get("reference_quote_is_fill") is not False):
        failures.append("Synthetic recommendation must not imply execution approval or a fill")

    source_path = ROOT / "assets/diagrams/production-architecture.mmd"
    source = source_path.read_text(encoding="utf-8")
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
    svg_text = source_path.with_suffix(".svg").read_text(encoding="utf-8")
    svg = ET.fromstring(svg_text)
    namespace = {"s": "http://www.w3.org/2000/svg"}
    if f"source-sha256:{digest}" not in svg_text:
        failures.append("Canonical SVG must be regenerated after a Mermaid source change")
    if svg.find("s:title", namespace) is None or svg.find("s:desc", namespace) is None:
        failures.append("Canonical SVG needs an accessible title and description")
    for element in svg.iter():
        if element.tag.split("}")[-1] in ("script", "foreignObject"):
            failures.append("Canonical SVG must remain static and self-contained")
        for attribute, value in element.attrib.items():
            if attribute.split("}")[-1] in ("href", "src") and not value.startswith("#"):
                failures.append("Canonical SVG must not load external resources")

    readme_words = len((ROOT / "README.md").read_text(encoding="utf-8").split())
    if not 350 <= readme_words <= 500:
        failures.append(f"README has {readme_words} words; expected 350–500")
    if len(list((ROOT / "assets/diagrams").glob("*.mmd"))) != 1:
        failures.append("Keep one canonical Mermaid architecture source")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"PASS: {len(markdown)} Markdown files, {link_count} local links, "
          f"{len(json_files)} JSON files, canonical SVG/source, {readme_words} README words")


if __name__ == "__main__":
    validate()

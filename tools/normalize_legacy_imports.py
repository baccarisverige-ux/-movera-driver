from pathlib import Path

PKG = "movera_driver"

replacements = [
    ("package:riding_app/constants/", f"package:{PKG}/core/constants/"),
    ("package:riding_app/services/", f"package:{PKG}/core/services/"),
    ("package:riding_app/models/", f"package:{PKG}/shared/models/"),
    ("package:riding_app/widgets/", f"package:{PKG}/shared/widgets/"),
    ("package:riding_app/presentation/common/", f"package:{PKG}/shared/presentation/"),
    ("package:riding_app/presentation/driver/", f"package:{PKG}/features/driver/"),
    ("package:riding_app/", f"package:{PKG}/"),
]

for dart in list(Path("lib").rglob("*.dart")) + list(Path("test").rglob("*.dart")):
    if not dart.is_file():
        continue
    text = dart.read_text(errors="ignore")
    for old, new in replacements:
        text = text.replace(old, new)
    dart.write_text(text)

# Migration helpers are temporary and must not become canonical product source.
Path("tools/canonicalize.py").unlink(missing_ok=True)
Path(__file__).unlink(missing_ok=True)

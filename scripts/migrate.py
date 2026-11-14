#!/usr/bin/env python3
"""One-time rebrand: IPVIO Stream -> Universal IPTV Player (UIPTVP).

Run inside a checkout of the upstream project:  python3 scripts/migrate.py .
Idempotent: re-running on an already-migrated tree changes nothing.
"""
import os, shutil, sys

root = sys.argv[1] if len(sys.argv) > 1 else "."
os.chdir(root)

REPLACE = [
    ("Emrodev/IPVIO-Stream", "yashhasan570/UIPTVP"),
    ('Cat(AIcon.HeartFilled, "Spende", "Unterstütze IPVIO Stream")', 'Cat(AIcon.HeartFilled, "Kontakt", "Telegram")'),
    ("IPVIO-Stream.apk", "UIPTVP.apk"),
    ("ipvio-stream-debug", "uiptvp-debug"),
    ("IPVIO Stream", "Universal IPTV Player"),
    ("IPVIOStream/1.0", "UIPTVP/1.0"),
    ("IPVIO-Stream", "UIPTVP"),
    ("IPVIO v1.2", "UIPTVP v1.0"),
    ("IPVIO Diagnose", "Diagnostics"),
    ("IPVIO diagnostics", "Diagnostics"),
    ("IPVIO-diagnose", "diagnose"),
    ("Diagnóstico IPVIO", "Diagnóstico"),
    ("Diagnostic IPVIO", "Diagnostic"),
    ("Diagnostica IPVIO", "Diagnostica"),
    ("IPVIO tanılama", "tanılama"),
    ("IPVIO dijagnostika", "dijagnostika"),
    ("IPVIO Navy", "Navy"),
    ("IPVIO Lacivert", "Lacivert"),
    ("IPVIO tamnoplava", "tamnoplava"),
    ("IPVIO Azul marino", "Azul marino"),
    ("IPVIO Marine", "Marine"),
    ("IPVIO Blu notte", "Blu notte"),
    ('Text("IPVIO", color = Color.White, fontSize = 28.sp', 'Text("UIPTVP", color = Color.White, fontSize = 28.sp'),
    ('AccentPreset("IPVIO", BRAND_GREEN', 'AccentPreset("UIPTVP", BRAND_GREEN'),
    ('header("User-Agent", "IPVIO")', 'header("User-Agent", "UIPTVP")'),
    ('applicationId = "com.ipvio.stream"', 'applicationId = "com.uiptvp.stream"'),
    ('contains("ipvio", true)', 'contains("uiptvp", true)'),
    ('"ipvio.apk"', '"uiptvp.apk"'),
    ("the private IPVIO app", "the existing app"),
    ("<!-- IPVIO logo (image ic_logo_fg.png) for the adaptive app icon -->", "<!-- App logo (image ic_logo_fg.png) for the adaptive app icon -->"),
    ("<!-- App icon: background in the color of the IPVIO logo (almost black navy) -->", "<!-- App icon: background color (almost black navy) -->"),
    ("// Donate is always the very last entry", "// Contact is always the very last entry"),
    ("-> DonateSection(ctx)", "-> ContactSection(ctx)"),
    ('rootProject.name = "Universal IPTV Player"', 'rootProject.name = "UIPTVP"'),
]

TEXT_EXT = (".kt", ".xml", ".kts", ".properties", ".gitignore", ".yml")
DOC_FILES = ["docs/GOOGLE_DRIVE.md", "THIRD_PARTY_NOTICES.md"]

def walk():
    for r, dirs, files in os.walk("."):
        if ".git" in dirs:
            dirs.remove(".git")
        for f in files:
            yield os.path.join(r, f)

count = 0
for path in walk():
    norm = os.path.normpath(path)
    if path.endswith(TEXT_EXT) or norm in DOC_FILES:
        s = open(path, encoding="utf-8").read()
        o = s
        for a, b in REPLACE:
            s = s.replace(a, b)
        if s != o:
            open(path, "w", encoding="utf-8").write(s)
            count += 1
print("patched files:", count)

for f in ["CLAUDE.md", "CHANGELOG.md", "RELEASE_NOTES_1.1.md", "docs/RELEASE.md",
          ".github/FUNDING.yml", "docs/ARCHITECTURE.md", "docs/DIAGRAMS.md",
          "docs/REFACTORING-PROGRESS.md", "docs/SECURITY.md", "docs/SETTINGS.md",
          "docs/TECH-DEBT.md", "docs/TESTING.md"]:
    if os.path.exists(f):
        os.remove(f); print("removed", f)
for d in ["docs/adr", "docs/quality", "docs/tasks", "docs/screenshots"]:
    if os.path.isdir(d):
        shutil.rmtree(d); print("removed dir", d)

open("app/src/main/java/com/ipvio/stream/Donate.kt", "w", encoding="utf-8").write('package com.ipvio.stream\n\nimport android.content.Context\nimport androidx.compose.runtime.Composable\nimport androidx.compose.ui.text.font.FontWeight\nimport androidx.compose.ui.unit.sp\n\n/** Contact info of the maintainer (Telegram). */\nobject Contact {\n    const val HANDLE = "@johnconstantine570"\n    const val URL = "https://t.me/johnconstantine570"\n}\n\n/** Settings > Contact: maintainer handle and link (no button: TVs often have no browser). */\n@Composable\ninternal fun ContactSection(@Suppress("UNUSED_PARAMETER") ctx: Context) {\n    SectionTitle("Kontakt")\n    Hint("Universal IPTV Player is free, ad-free and open source (GPL-3.0). Questions or feedback? Reach the maintainer on Telegram.")\n    Text(Contact.HANDLE, color = Accent2, fontSize = 18.sp, fontWeight = FontWeight.Bold, raw = true)\n    Text(Contact.URL.removePrefix("https://"), color = Muted, fontSize = 15.sp, raw = true)\n}\n')
print("wrote Donate.kt (Contact section)")

open("README.md", "w", encoding="utf-8").write('# Universal IPTV Player (UIPTVP)\n\nA free, open-source IPTV player for Android TV, Google TV and Fire TV.\nSkip intro, cast pages, IMDb/Rotten Tomatoes ratings, profiles, picture-in-picture and split screen for two live streams.\n\nNo account, no ads, no content included: bring your own playlist (Xtream Codes login or M3U address).\n\n**Download:** [UIPTVP.apk (latest release)](https://github.com/yashhasan570/UIPTVP/releases/latest/download/UIPTVP.apk)\n\n## Build it yourself\n\nOpen the project in Android Studio and run `Build > Build APK(s)` for a debug APK.\nThe repository also ships a GitHub Actions workflow (`.github/workflows/build.yml`) that builds a debug APK on every push.\n\nOptional developer API keys (TMDB, OMDb, Google Drive backup) go into `secrets.properties` (see `secrets.properties.example`); normal users enter their own keys in the app under Settings > API keys.\n\n## Updates\n\nThe app checks for updates itself (bell icon in the app, automatic check on start).\nIt reads a small `update.json` attached to the latest GitHub release of this repository:\n\n```json\n{"versionCode": 7, "versionName": "1.4.2", "apk": "UIPTVP.apk", "sha256": "<lowercase hex sha256 of the apk>", "notes": "what changed"}\n```\n\nAttach `update.json` and the signed APK (same signing key as the installed app) to a GitHub release; the built-in update check then offers the new version.\nA custom update address can also be set in the app under Settings > Updates.\n\n## Contact\n\nQuestions or feedback: Telegram [@johnconstantine570](https://t.me/johnconstantine570)\n\n## License\n\nUniversal IPTV Player is free software, based on the open-source IPVIO Stream project, and is licensed under the GNU General Public License v3 (see LICENSE). The GPL applies because the app includes the GPL-3.0 licensed FFmpeg audio decoder.\nThe software is provided "as is", without warranty of any kind. It contains no channels, playlists, films or series and is only a player for playlists you add yourself.\n')
print("wrote README.md")

# Universal IPTV Player (UIPTVP)

A free, open-source IPTV player for Android TV, Google TV and Fire TV.
Skip intro, cast pages, IMDb/Rotten Tomatoes ratings, profiles, picture-in-picture and split screen for two live streams.

No account, no ads, no content included: bring your own playlist (Xtream Codes login or M3U address).

**Download:** [UIPTVP.apk (latest release)](https://github.com/yashhasan570/UIPTVP/releases/latest/download/UIPTVP.apk)

## Build it yourself

Open the project in Android Studio and run `Build > Build APK(s)` for a debug APK.
The repository also ships a GitHub Actions workflow (`.github/workflows/build.yml`) that builds a debug APK on every push.

Optional developer API keys (TMDB, OMDb, Google Drive backup) go into `secrets.properties` (see `secrets.properties.example`); normal users enter their own keys in the app under Settings > API keys.

## Updates

The app checks for updates itself (bell icon in the app, automatic check on start).
It reads a small `update.json` attached to the latest GitHub release of this repository:

```json
{"versionCode": 7, "versionName": "1.4.2", "apk": "UIPTVP.apk", "sha256": "<lowercase hex sha256 of the apk>", "notes": "what changed"}
```

Attach `update.json` and the signed APK (same signing key as the installed app) to a GitHub release; the built-in update check then offers the new version.
A custom update address can also be set in the app under Settings > Updates.

## Contact

Questions or feedback: Telegram [@johnconstantine570](https://t.me/johnconstantine570)

## License

Universal IPTV Player is free software, based on the open-source IPVIO Stream project, and is licensed under the GNU General Public License v3 (see LICENSE). The GPL applies because the app includes the GPL-3.0 licensed FFmpeg audio decoder.
The software is provided "as is", without warranty of any kind. It contains no channels, playlists, films or series and is only a player for playlists you add yourself.

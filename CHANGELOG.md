# Changelog

## v2.0

### Bug fixes
- **Admin commands now work.** `admin.py` was never registered in `bot.py`,
  so `/vpsstatus`, `/addprem`, `/removeprem` and `/premlist` did nothing.
  Registered it.
- **Auto-restart no longer deadlocks.** The background monitor called
  `deploy.restart_bot` while a `bots.db` write transaction was still open,
  causing `database is locked` and silently killing auto-restart. Writes are
  now short, isolated transactions and the restart runs outside them.
- **Settings toggles are honored.** `notify_on_crash` and `auto_fix_enabled`
  from the Settings menu were written but never read — the monitor always
  notified and always auto-fixed. It now respects both per-user.
- **Premium expiry is timezone-safe.** Replaced deprecated
  `datetime.utcnow()` with timezone-aware datetimes, and made expiry
  comparison tolerant of older naive timestamps (no more aware/naive
  `TypeError`).
- **File-handle leaks fixed** in the file browser and backup sender
  (`open()` results are now closed via `with`), and downloads carry a
  proper filename.

### Config
- `BOT_TOKEN` was only the numeric bot-id half (`8610655917`) — not a usable
  token, so the bot could never authenticate. It's now a clearly-marked
  empty placeholder: paste your **full** `123456789:AAH…` token from
  @BotFather.
- Added `VERSION` (shown on the home screen).

### Small additions
- `/help` now opens the main menu (alias of `/start`).

## v2.1

### Colorful buttons
- Bumped `python-telegram-bot` from `21.6` to `>=22.7,<23` — 21.6 predates
  PTB's support for Telegram's button `style` field (added in PTB 22.7;
  Telegram's Bot API added the field itself in 9.4). Passing `style=` on
  21.6 would raise a `TypeError`, so this bump is required, not optional.
- Colored every actionable inline button:
  - 🟢 green (`success`): create / positive actions — Upload, Deploy from
    GitHub, Start/Restart, Try Auto-Fix, Add/Update env var, Cancel (in
    delete confirmation), and ON-state settings toggles.
  - 🔵 blue (`primary`): main navigation — My Bots, Files, Logs, Env Vars,
    Dashboard, Backup, Settings, Account, per-bot Logs/Stats.
  - 🔴 red (`danger`): destructive / stop actions — Stop, Delete, the
    "Yes, delete" confirm, and OFF-state settings toggles.
  - Back/Cancel-navigation and the Channel/YouTube link buttons were left
    uncolored on purpose — Telegram's own default look is what actually
    reads as "secondary" next to colored actions, so leaving them plain
    keeps the buttons that matter from getting lost in a wall of color.

⚠️ Heads-up: I verified the `style=` usage against PTB's own documented
API and compiled every file, but this sandbox has no network access, so I
could not `pip install python-telegram-bot>=22.7` here and run a live
smoke test against Telegram's servers. Run `pip install -r
requirements.txt --upgrade` in a venv and test `/start` once before
relying on this in production — if PTB 22 changed anything else you
depend on, it'll show up there.

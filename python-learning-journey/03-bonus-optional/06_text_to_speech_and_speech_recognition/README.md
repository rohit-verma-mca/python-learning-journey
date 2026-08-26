# Text-to-Speech & Speech Recognition

**Source:** Book Ch.24

## Concepts covered
- Text-to-speech with `pyttsx3` (works fully offline)
- Speech-to-text with `speech_recognition` (usually needs an internet-based engine like Google's)
- Adjusting voice properties: rate, volume, voice selection
- Capturing microphone input and converting it to text
- Basic voice-command style program structure

## My Notes
`pyttsx3` converts text into spoken audio completely offline, using the operating
system's own built-in voices — no internet or API key needed, which makes it the
simpler and more reliable half of this topic. `speech_recognition` does the opposite
(audio to text), but most of its recognizer backends need an internet connection since
they send the audio to a cloud service to be transcribed. Together these two form the
building blocks of a basic voice assistant, even a very simple one.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Text-to-Speech Reader | ⬜ |
| 2 | Simple Voice Command Recognizer | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../../EXERCISE_FORMAT.md).
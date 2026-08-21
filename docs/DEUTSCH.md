# Voice-Agent → Voltwerk-Clerk (Deutsch)

Das Repo ist noch die Render/LiveKit-Insurance-Demo (Englisch, OpenAI, Render Workflows).

## Was jetzt gilt

| Ohne Keys | Mit Keys (später) |
|-----------|-------------------|
| Clerk in der VOLTWERK-App: Mikrofon + Text, Katalog, optional xAI | `agent/cr404_clerk.py` als LiveKit-Agent, `AGENT_MODE=voltwerk` |
| Keine LiveKit-Rechnung | LIVEKIT_* + LLM-Key |

## Env (Platzhalter, nicht committen)

```
AGENT_MODE=voltwerk
LIVEKIT_URL=
LIVEKIT_API_KEY=
LIVEKIT_API_SECRET=
# LLM: lieber XAI_API_KEY / OpenAI-kompatibel api.x.ai
OPENAI_API_KEY=
```

Insurance-Demo nicht löschen, bis der Clerk auf LiveKit getestet ist.

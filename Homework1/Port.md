# 1. Port

## What is a Port?

A **port** is a communication endpoint that allows applications to send and receive data over a network. An **IP address** identifies the device, while a **port** identifies the specific application on that device.

## Common Ports

| Port | Service |
|------|---------|
| 80 | HTTP |
| 443 | HTTPS |
| 22 | SSH |
| 5432 | PostgreSQL |
| 8501 | Streamlit |

## Streamlit Example

Run:

```bash
streamlit run app.py
```

Output:

```text
http://localhost:8501
```

Here, **8501** is the default port used by Streamlit.

## Key Points

- Port identifies an application or service.
- IP identifies the device.
- Multiple applications use different ports.
- Streamlit runs on **Port 8501** by default.
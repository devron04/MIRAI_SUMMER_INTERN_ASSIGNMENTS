# Streamlit Functions

## 1. `st.title()`
Displays the main title.

```python
st.title("My App")
```

---

## 2. `st.header()`
Displays a section heading.

```python
st.header("Student Details")
```

---

## 3. `st.subheader()`
Displays a smaller heading.

```python
st.subheader("Personal Information")
```

---

## 4. `st.write()`
Displays text, variables, tables, and other objects.

```python
st.write("Welcome to Streamlit!")
```

---

## 5. `st.text()`
Displays plain text.

```python
st.text("This is plain text.")
```

---

## 6. `st.markdown()`
Displays formatted Markdown text.

```python
st.markdown("**Bold Text**")
```

---

## 7. `st.text_input()`
Accepts text input from the user.

```python
name = st.text_input("Enter your name")
```

---

## 8. `st.number_input()`
Accepts numeric input.

```python
age = st.number_input("Enter your age")
```

---

## 9. `st.text_area()`
Accepts multi-line text input.

```python
msg = st.text_area("Enter your message")
```

---

## 10. `st.selectbox()`
Creates a dropdown menu.

```python
course = st.selectbox("Select Course", ["AI", "ML", "DS"])
```

---

## 11. `st.radio()`
Creates radio buttons.

```python
gender = st.radio("Gender", ["Male", "Female"])
```

---

## 12. `st.checkbox()`
Creates a checkbox.

```python
agree = st.checkbox("I Agree")
```

---

## 13. `st.slider()`
Creates a slider.

```python
age = st.slider("Select Age", 18, 60)
```

---

## 14. `st.button()`
Creates a clickable button.

```python
if st.button("Submit"):
    st.write("Submitted")
```

---

## 15. `st.success()`
Displays a success message.

```python
st.success("Success!")
```

---

## 16. `st.error()`
Displays an error message.

```python
st.error("Something went wrong!")
```

---

## 17. `st.warning()`
Displays a warning message.

```python
st.warning("Please check your input.")
```

---

## 18. `st.info()`
Displays an informational message.

```python
st.info("This is an information message.")
```

---

## 19. `st.image()`
Displays an image.

```python
st.image("image.png")
```

---

## 20. `st.file_uploader()`
Uploads files.

```python
file = st.file_uploader("Upload a file")
```

---

## 21. `st.code()`
Displays formatted code.

```python
st.code("print('Hello World')")
```

---

## 22. `st.dataframe()`
Displays a data table.

```python
st.dataframe(data)
```

---

## 23. `st.sidebar`
Creates widgets in the sidebar.

```python
st.sidebar.title("Menu")
```

---

## 24. `st.columns()`
Creates multiple columns.

```python
col1, col2 = st.columns(2)
```

---

## 25. `st.metric()`
Displays a metric with an optional change indicator.

```python
st.metric("Temperature", "30°C", "+2°C")
```

---

# Summary Table

| Function | Purpose |
|----------|---------|
| `st.title()` | Main title |
| `st.header()` | Heading |
| `st.subheader()` | Subheading |
| `st.write()` | Display text/data |
| `st.text()` | Plain text |
| `st.markdown()` | Formatted Markdown |
| `st.text_input()` | Text input |
| `st.number_input()` | Number input |
| `st.text_area()` | Multi-line text |
| `st.selectbox()` | Dropdown |
| `st.radio()` | Radio buttons |
| `st.checkbox()` | Checkbox |
| `st.slider()` | Slider |
| `st.button()` | Button |
| `st.success()` | Success message |
| `st.error()` | Error message |
| `st.warning()` | Warning message |
| `st.info()` | Information message |
| `st.image()` | Display image |
| `st.file_uploader()` | Upload files |
| `st.code()` | Display code |
| `st.dataframe()` | Display DataFrame |
| `st.sidebar` | Sidebar |
| `st.columns()` | Create columns |
| `st.metric()` | Display metrics |
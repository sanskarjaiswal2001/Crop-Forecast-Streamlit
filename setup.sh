mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCURS = false\n\
\n\
" > ~/.streamlit/config.toml

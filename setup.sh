rm ~/.streamlit/config.toml
rm ~/.streamlit/credentials.toml
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"jean.ivars@ensait.fr\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml

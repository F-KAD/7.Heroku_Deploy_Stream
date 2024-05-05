#web: sh setup.sh && streamlit run stream.py
web: sh setup.sh && gunicorn --timeout 180 stream:app
#web: sh setup.sh && streamlit run test_view.py
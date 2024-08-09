import streamlit as st
import os
import numpy as np
import json
import requests

# Define the Streamlit form
st.title("Document Import Form")

with st.form("import_form"):
    ressort_prod = st.text_input("Ressort Prod", "77028529")
    ressort_stage = st.text_input("Ressort Stage", "3")
    author_prod = st.text_input("Author Prod", "77082905")
    author_stage = st.text_input("Author Stage", "23504")
    text1 = st.text_area("Text 1", "1.1_streamlit another text paragraph Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.")
    text2 = st.text_area("Text 2", "2.1_streamlit another text paragraph Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.")
    
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    # Load the environment variable and document id
    env = os.getenv('APP_ENV', 'stage')  # Default to 'stage' if not set

    # Load the configurations from the config file
    with open('../api/env_config.json') as config_file:
        config = json.load(config_file)
        environment_config = config['environments'][env]

    # Construct the URL based on the environment
    domain = environment_config['domain']
    url = f"{domain}/proxy/api/api/v1/import/documents"

    # Use the auth details directly from the configuration
    headers = environment_config['auth']

    # Base object template
    timestamp = "2024-08-09T13:48:00.850Z"

    # Data payload with dynamically generated documents
    data = {
        "systemName": "dokue",
        "webhook": "https://my-domain.com/webhooks/document-import",
        "context": {
            "myIdentifier": "dokue-import"
        },
        "documents": [
            {
                "id": "22222223",
                "title": "test import",
                "contentType": "article-bawu",
                "checksum": "22222225",
                "publishControl": {
                    "firstPublicationDate": timestamp,
                    "significantPublicationDate": timestamp,
                    "lastPublicationDate": timestamp,
                },
                "content": [{'component': 'article-container',
                            'identifier': 'p:1:1.article-container',
                            'id': 'doc-1i49k6g4f0',
                            'position': 'fixed',
                            'containers': {'header': [{'component': 'head',
                                                        'identifier': 'p:1:1.head',
                                                        'id': 'doc-1i49k6g4f1',
                                                        'content': {'overline': 'overline',
                                                                    'title': 'artikel_import_v1',
                                                                    'text': 'teaser',
                                                                    'place': 'ort',
                                                                    'authors': 'Florian Huth',
                                                                    'headerInfo': {'service': 'headerInfo', 'params': {}}},
                                                        'position': 'fixed'}],
                                           'main': [{'component': 'paragraph',
                                                     'identifier': 'p:1:1.paragraph',
                                                     'id': 'doc-1i49k6g4g1',
                                                     'content': {'text': text1}},
                                                    {'component': 'subtitle',
                                                     'identifier': 'p:1:1.subtitle',
                                                     'id': 'doc-1i49k7o2q0',
                                                     'content': {'title': 'h2 title'}},
                                                    {'component': 'paragraph',
                                                     'identifier': 'p:1:1.paragraph',
                                                     'id': 'doc-1i49k83ot0',
                                                     'content': {'text': text2}},
                                                    {'component': 'bullet-list',
                                                     'identifier': 'p:1:1.bullet-list',
                                                     'id': 'doc-1i49k8i5o0',
                                                     'containers': {'list': [{'component': 'bullet-list-item',
                                                                             'identifier': 'p:1:1.bullet-list-item',
                                                                             'id': 'doc-1i49k8i5o1',
                                                                             'content': {'text': 'some bullet points 1'}},
                                                                            {'component': 'bullet-list-item',
                                                                             'identifier': 'p:1:1.bullet-list-item',
                                                                             'id': 'doc-1i49k8voo0',
                                                                             'content': {'text': 'some bullet points 2'}},
                                                                            {'component': 'bullet-list-item',
                                                                             'identifier': 'p:1:1.bullet-list-item',
                                                                             'id': 'doc-1i49k97ms0',
                                                                             'content': {'text': 'some bullet points 3'}},
                                                                            {'component': 'bullet-list-item',
                                                                             'identifier': 'p:1:1.bullet-list-item',
                                                                             'id': 'doc-1i49k991p0',
                                                                             'content': {'text': 'some bullet points 4'}},
                                                                            {'component': 'bullet-list-item',
                                                                             'identifier': 'p:1:1.bullet-list-item',
                                                                             'id': 'doc-1i49k9asu0',
                                                                             'content': {'text': 'some bullet points 5'}}]}}]}}],
                "design": {'name': 'p:1:1', 'version': '25.0.0'},
                "metadata": {
                    'sourcePublication': 'swp',
                    'ressorts-swp': {'$ref': 'documents', 'references': [{'id': ressort_stage}]},
                    'title': 'artikel_import_v1',
                    'reward': {'isFree': True},
                    'reward-infobox': {'isFree': True},
                    'authors': {'$ref': 'documents', 'references': [{'id': author_stage}]},
                    'print-publication-date': {'isSetToTomorrow': True},
                    'autoListing': True,
                    'payCategory': 'free',
                    'status': '17601',
                    'userneeds-swp': 4,
                    'print-ressort-swp': {'$ref': 'document',
                                          'reference': {'id': ressort_prod},
                                          'interredShortname': 'CR_BLIK',
                                          'wasOverwritten': False},
                    'type': 'article',
                    'teaserTitle': 'artikel_import_v1',
                    'printTitle': 'title',
                    'overline': 'overline',
                    'robots': 'index, follow, noarchive',
                    'dependencies': {},
                    'printHeadline': 'teaser',
                    'description': 'teaser',
                    'place': 'ort',
                    'slug': 'overline-title'
                },
                "flags": {
                    "autoPublish": False
                }
            }
        ]
    }

    json_data = json.dumps(data)
    st.json(data)

    # Making the POST request
    response = requests.post(url, headers=headers, json=data, verify=True)

    # Printing the response
    st.write(response.json())

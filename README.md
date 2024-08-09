# cardiovascular-diseases-ditection-api

It's is a free online REST API that you can use to ditect cardiovascular diseases.

## Installation

Clone reposity from GitHub
```
git clone https://github.com/mamun-swe/cardiovascular-diseases-ditection-api
```

Install required dependencies
```
pip install -r requirements.txt
```

Start app via this CLI command

```
fastapi dev main.py
```

Browse the given URL to your browser

```
http://127.0.0.1:8000/test-result
```

Response will be looks like this:

```json
{
  "randon_forest_classifier_result": 0.9833333333333333,
  "decission_tree_classifier_result": 0.9766666666666667,
  "support_vector_machine_result": 0.6
}
```
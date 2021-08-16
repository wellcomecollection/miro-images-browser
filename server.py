#!/usr/bin/env python

from flask import Flask, request, render_template
try:
    import httpx
except ImportError:
    import requests as httpx

app = Flask(__name__)


@app.template_filter("miro_id")
def miro_id(work):
    return next(
        id for id in work['identifiers'] if id['identifierType']['id'] == 'miro-image-number'
    )['value']


@app.template_filter("license")
def license(work):
    for item in work['items']:
        for location in item['locations']:
            if location['locationType']['id'] == 'iiif-image':
                return location['license']['id']


@app.route("/")
def index():
    license = request.args.get("license", "")
    dateTo = request.args.get("dateTo", "")
    dateFrom = request.args.get("dateFrom", "")
    query = request.args.get("query", "")
    page = int(request.args.get("page", "1"))

    params = {"pageSize": 100, "include": "identifiers,items", "items.locations.locationType": "iiif-image",
"page": page}

    if license:
        params["items.locations.license"] = license
    if dateTo:
        params["production.dates.to"] = dateTo
    if dateFrom:
        params["production.dates.from"] = dateFrom
    if query:
        params["query"] = query

    resp = httpx.get("https://api.wellcomecollection.org/catalogue/v2/works", params=params)
    resp.raise_for_status()

    return render_template("index.html", resp=resp.json(), license=license, dateTo=dateTo, dateFrom=dateFrom, api_url=resp.url, page=page, query=query)


if __name__ == '__main__':
    app.run(port=6737, debug=True)

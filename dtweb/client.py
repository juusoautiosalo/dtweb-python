"""Client for the Digital Twin Web

A client library with functions for accessing DT documents
around the Digital Twin Web.
"""
import requests

def fetch_host_url(dtid: str) -> str:
    """
    Fetches the hosting URL of a DT document based on a DTID.

    Args:
      dtid: The DT identifier of the target DT. Must be URL.

    Returns:
      The hosting URL of the DT.

    """

    r = requests.get(dtid)
    return r.url

def fetch_dt_doc(dtid: str) -> dict:
    """
    Fetches DT doc in dict form based on a DTID.

    Args:
      dtid: The DT identifier of the target DT. Must be URL.

    Returns:
      DT doc in python dict form.

    """

    dt_url = fetch_host_url(dtid)
    r = requests.get(dt_url + '/index.json')
    return r.json()

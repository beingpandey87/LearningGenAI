from semantic_chunker import get_chunker
import numpy as np
from typing import List, Tuple
import re

document = """
Kubernetes is a container orchestration platform that automates deployment,
scaling, and management of containerized applications. It was originally
designed by Google and is now maintained by the Cloud Native Computing Foundation.

The core concept in Kubernetes is the Pod. A Pod is the smallest deployable
unit and can contain one or more containers. Pods share storage and network
resources, making them ideal for tightly coupled application components.

Deployments provide declarative updates for Pods. You describe a desired state
in a Deployment, and the Deployment controller changes the actual state to
match. This enables rolling updates, rollbacks, and scaling operations.

Monitoring Kubernetes clusters requires collecting metrics from multiple
sources. The Metrics Server provides resource metrics like CPU and memory
usage. For comprehensive observability, you need to integrate with systems
like Prometheus for metrics, Jaeger for traces, and a log aggregator.
"""
def chunker(content:str):
    # Initialize chunker with tuned parameters
    chunker = get_chunker(
        "gpt-3.5-turbo",
        chunking_type="text",  # required
        max_tokens=100,  # required
        trim=False,  # default True
        overlap=5,  # default 0
    )

    chunks = chunker.chunks(content)

    print(f"Document split into {len(chunks)} semantic chunks:\n")
    for i, chunk in enumerate(chunks, 1):
        print(f"--- Chunk {i} ({len(chunk)} chars) ---")
        print(chunk)
        print("-------------------------------------------")

if __name__ == "__main__":
    chunker(document)
[![Build Status](https://travis-ci.com/usdot-jpo-sdc/sdc-dot-waze-get-manifests-for-persistence.svg?branch=master)](https://travis-ci.com/usdot-jpo-sdc/sdc-dot-waze-get-manifests-for-persistence)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=usdot-jpo-sdc_sdc-dot-waze-get-manifests-for-persistence&metric=alert_status)](https://sonarcloud.io/dashboard?id=usdot-jpo-sdc_sdc-dot-waze-get-manifests-for-persistence)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=usdot-jpo-sdc_sdc-dot-waze-get-manifests-for-persistence&metric=coverage)](https://sonarcloud.io/dashboard?id=usdot-jpo-sdc_sdc-dot-waze-get-manifests-for-persistence)
# sdc-dot-waze-get-manifests-for-persistence
This lambda function is responsible for getting the manifest file for a batch Id from DynamoDB during the data persistence process.

<a name="toc"/>

## Table of Contents

[I. Release Notes](#release-notes)

[II. Overview](#overview)

[III. Design Diagram](#design-diagram)

[IV. Getting Started](#getting-started)

[V. Unit Tests](#unit-tests)

[VI. Support](#support)

---

<a name="release-notes"/>


## [I. Release Notes](ReleaseNotes.md)
TO BE UPDATED

<a name="overview"/>

## II. Overview

There are two primary functions that this lambda function serves:
* **get_manifests_to_process** - gets the manifest record from dynamoDB for a batchId


<a name="design-diagram"/>

## III. Design Diagram

![sdc-dot-waze-get-manifests-for-persistence](images/waze-data-persistence.png)


<a name="getting-started"/>

## IV. Getting Started

The following instructions describe the procedure to build and deploy the lambda.

### Prerequisites
* NA 

---
### ThirdParty library

*NA

### Licensed softwares

*NA

### Programming tool versions

*Python 3.6


---
### Build and Deploy the Lambda

#### Build Process

**Step 1**: Setup virtual environment on your system by foloowing below link
https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#with-s3-example-deployment-pkg-python

**Step 2**: Create a script with below contents e.g(sdc-dot-waze-get-manifests-for-persistence.sh)
```#!/bin/sh

cd sdc-dot-waze-get-manifests-for-persistence
zipFileName="sdc-dot-waze-get-manifests-for-persistence.zip"

zip -r9 $zipFileName common/*
zip -r9 $zipFileName lambdas/*
zip -r9 $zipFileName README.md
zip -r9 $zipFileName get_manifests_to_process_handler_main.py
```

**Step 3**: Change the permission of the script file

```
chmod u+x sdc-dot-waze-get-manifests-for-persistence.sh
```

**Step 4** Run the script file
./sdc-dot-waze-get-manifests-for-persistence.sh

**Step 5**: Upload the sdc-dot-waze-get-manifests-for-persistence.zip generated from Step 4 to a lambda function via aws console.

[Back to top](#toc)

---
<a name="unit-tests"/>

## V. Unit Tests

TO BE UPDATED

---
<a name="support"/>

## VI. Support

For any queries you can reach to support@securedatacommons.com
---
[Back to top](#toc)
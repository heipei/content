#!/usr/bin/env bash

# exit on errors
set -e

SECRET_CONF_PATH=$(cat secret_conf_path)
CONF_PATH="./Tests/conf.json"

IS_NIGHTLY=false

if [ -f create_instances_build_num.txt ]; then
  PREVIOUS_JOB_NUMBER=`cat create_instances_build_num.txt`
fi
# TODO: Add version of the test with SSL and without SSL
python3 ./Tests/configure_and_test_integration_instances.py -u "$USERNAME" -p "$PASSWORD" -c "$CONF_PATH" -s "$SECRET_CONF_PATH" -g "$GIT_SHA1" --ami_env "$1" -n $IS_NIGHTLY --branch "$CIRCLE_BRANCH" --build-number "$PREVIOUS_JOB_NUMBER" -sa "$GCS_PATH" -l
if [ -f ./Tests/test_pack.zip ]; then
  cp ./Tests/test_pack.zip $CIRCLE_ARTIFACTS
fi

#!/usr/bin/env bash
cp test.settings .env

pytest -x $@

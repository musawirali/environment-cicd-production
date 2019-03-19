#!/bin/bash
sops -d jerry2jx-env-prod.enc.env | sort  > jerry2jx-env-prod.env
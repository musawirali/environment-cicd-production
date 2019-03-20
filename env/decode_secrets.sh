#!/bin/sh
sops -d jerry2jx-env-prod.enc.env | sort  > ./envs/jerry2__secretValues.env
sops -d aws-snapshot.enc.env | sort  > ./envs/jerry2__rdsSnapshotCreds.env
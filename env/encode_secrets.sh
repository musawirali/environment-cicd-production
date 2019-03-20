#!/bin/sh
sops -e ./envs/jerry2__secretValues.env > jerry2jx-env-prod.enc.env
sops -e ./envs/jerry2__rdsSnapshotCreds.env > aws-snapshot.enc.env
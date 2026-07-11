#!/usr/bin/env bash
set -euo pipefail

BACKUP_DIR="${BACKUP_DIR:-$HOME/smart-parking-backups}"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

docker exec smart-parking-db mysqldump -uroot -p"${MYSQL_ROOT_PASSWORD}" "${MYSQL_DATABASE}" > "$BACKUP_DIR/smart_parking_${TIMESTAMP}.sql"

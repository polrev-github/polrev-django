#!/bin/bash
mc alias set local http://127.0.0.1:9000 polrev polrev123

# Create folder-like structures by uploading a zero-byte file
echo "Initializing folder structure in default buckets..."
mc cp --attr x-amz-meta-custom-key=value /dev/null local/polrev/media/.keep
mc cp --attr x-amz-meta-custom-key=value /dev/null local/polrev/static/.keep

echo "Folder structure initialized."

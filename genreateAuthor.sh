#!/bin/bash

OUTPUT_FILE="AUTHORS"

github_users=()


# Use Git log to get a list of email addresses from the commit history
cat > "AUTHORS" <<- EOF
	# This file lists all contributors to the repository.

	$(git -C "$ROOTDIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf)
EOF
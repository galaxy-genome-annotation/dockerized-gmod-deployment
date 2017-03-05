#!/bin/bash
set -ex
rm -rf $JBROWSE_DATA;
cp -Rv /data/ $JBROWSE_DATA;
cp -Rv /data/PostGraphQL /jbrowse/plugins/;
echo '[ plugins.PostGraphQL  ]' >> /jbrowse/jbrowse.conf;
echo 'location = plugins/PostGraphQL' >> /jbrowse/jbrowse.conf

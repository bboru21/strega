# bash

if [[ ! -e urls.py ]]; then
    echo 'Creating urls.py'
    touch urls.py
    CUSTOMTAB="    " # 4 space tab
    echo "# enter ABC store product urls here\n\nURLS = [\n$CUSTOMTAB'https://www.abc.virginia.gov/products/cordials/liquore-strega#/product?productSize=0',\n]" > urls.py
fi

if [[ ! -e settings_local.py ]]; then
    echo 'Creating settings_local.py'
    touch settings_local.py
    echo 'from settings_base import *' > settings_local.py
fi

virtualenv virtualenv --no-site-packages && source virtualenv/bin/activate && pip install -r requirements.txt

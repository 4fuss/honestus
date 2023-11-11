# Odoo addons [Honestus dev assignement]

## Code quality

Code quality is assured via use of `flake8` and `OCA/pylint-odoo` linters. The
linters are run by [pre-commit](https://pre-commit.com/) tool.


## Task 1

Task 1 is implemented in [auth signup controller](addons/honestus_tweaks/controllers/auth_signup.py) and [related view templates](addons/honestus_tweaks/views/templates.xml).

## Task 2

Task 2 is implemented in [product model](addons/honestus_tweaks/models/product.py) and related [tests](addons/honestus_tweaks/tests/test_product.py).

## Task 3

Sale Order report is extended in [template](addons/honestus_tweaks/views/sale_order_report_template.xml). Product display name is redefined in [product model](addons/honestus_tweaks/models/product.py). Product display name is covered by [tests](addons/honestus_tweaks/tests/test_product.py).

## Task 4

Report is defined [here](addons/honestus_tweaks/report).

## Task 5 - Solution Design

There is OCA's [queue_job_cron](https://github.com/OCA/queue/tree/16.0/queue_job_cron) module which can solve issue with long running background jobs. It runs on separate thread so it doesn't affect Odoo's web workers.
Implementation estimation: 2 days.

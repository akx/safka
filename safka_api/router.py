import os

from lepo.router import Router

import safka_api.handlers.location

router = Router.from_file(filename=os.path.join(os.path.dirname(__file__), "openapi.yaml"))
router.add_handlers(safka_api.handlers.location)

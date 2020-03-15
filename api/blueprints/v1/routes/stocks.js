const express = require("express");
const router = express.Router();
const checkAuth = require('../middleware/check-auth');


const controller = require('../controllers/stocks');

// Handle incoming GET requests to /orders
router.get("/", checkAuth, controller.get_all);

router.put("/:id", checkAuth, controller.create);

router.get("/:id", checkAuth, controller.get);

router.delete("/:id", checkAuth, controller.delete);

module.exports = router;

// migrations/2_deploy_contracts.js
const ShipmentContract = artifacts.require("ShipmentContract");

module.exports = function(deployer) {
  deployer.deploy(ShipmentContract);
};

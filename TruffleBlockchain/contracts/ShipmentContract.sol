// contracts/ShipmentContract.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ShipmentContract {
    struct Shipment {
        uint256 shipmentId;
        uint256 netWeight;
        address[] stakeholders;
        uint256 shipmentValue;
    }

    mapping(uint256 => Shipment) public shipments;
    uint256 public shipmentCount;

    event ShipmentAdded(uint256 shipmentId);

    function addShipment(uint256 _netWeight, address[] memory _stakeholders, uint256 _shipmentValue) public {
        shipmentCount++;
        shipments[shipmentCount] = Shipment(shipmentCount, _netWeight, _stakeholders, _shipmentValue);
        emit ShipmentAdded(shipmentCount);
    }

    function getAllShipments() public view returns (Shipment[] memory) {
        Shipment[] memory allShipments = new Shipment[](shipmentCount);
        for (uint256 i = 1; i <= shipmentCount; i++) {
            allShipments[i - 1] = shipments[i];
        }
        return allShipments;
    }
}

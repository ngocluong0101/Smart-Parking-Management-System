import { DataTable } from "../components/DataTable";

const vehicles = [
  {
    id: 1,
    plate_number: "29A-12345",
    vehicle_type: "car",
    brand: "Toyota",
    color: "White",
  },
  {
    id: 2,
    plate_number: "59B1-56789",
    vehicle_type: "motorbike",
    brand: "Honda",
    color: "Red",
  },
];

export function VehiclePage() {
  return (
    <section className="panel">
      <div className="panel-header">
        <h3>Vehicle Management</h3>
        <span className="panel-badge">CRUD ready</span>
      </div>
      <DataTable
        columns={[
          { key: "plate_number", label: "Plate Number" },
          { key: "vehicle_type", label: "Type" },
          { key: "brand", label: "Brand" },
          { key: "color", label: "Color" },
        ]}
        rows={vehicles}
        emptyMessage="No vehicles found"
      />
    </section>
  );
}

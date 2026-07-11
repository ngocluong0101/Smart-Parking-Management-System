import { DataTable } from "../components/DataTable";

const history = [
  {
    plate: "29A-12345",
    checkIn: "08:00",
    checkOut: "09:30",
    duration: "90 min",
    fee: "20000 VND",
  },
  {
    plate: "59B1-56789",
    checkIn: "09:10",
    checkOut: "11:15",
    duration: "125 min",
    fee: "10000 VND",
  },
];

export function ParkingHistoryPage() {
  return (
    <section className="panel">
      <div className="panel-header">
        <h3>Parking History</h3>
        <span className="panel-badge">Audit trail</span>
      </div>
      <DataTable
        columns={[
          { key: "plate", label: "Plate" },
          { key: "checkIn", label: "Check-in" },
          { key: "checkOut", label: "Check-out" },
          { key: "duration", label: "Duration" },
          { key: "fee", label: "Fee" },
        ]}
        rows={history}
        emptyMessage="No history available"
      />
    </section>
  );
}

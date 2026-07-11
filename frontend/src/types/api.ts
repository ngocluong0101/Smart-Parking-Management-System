export type VehicleType = "car" | "motorbike" | "bicycle" | "truck" | "other";

export interface Vehicle {
  id: number;
  plate_number: string;
  vehicle_type: VehicleType;
  brand?: string | null;
  color?: string | null;
  owner_name?: string | null;
  created_at: string;
  updated_at: string;
}

export interface ParkingSession {
  id: number;
  vehicle_id: number;
  parking_lot_id: number;
  parking_fee_id: number;
  plate_raw?: string | null;
  plate_normalized: string;
  vehicle_type_snapshot: VehicleType;
  status: "active" | "closed" | "duplicate" | "invalid";
  check_in_time: string;
  check_out_time?: string | null;
  duration_minutes: number;
  total_fee: string;
  entry_image_path?: string | null;
  exit_image_path?: string | null;
  notes?: string | null;
  created_at: string;
  updated_at: string;
}

export interface DashboardSummary {
  active_sessions: number;
  total_sessions_today: number;
  total_revenue_today: string;
  motorbike_count: number;
  car_count: number;
  other_vehicle_count: number;
}

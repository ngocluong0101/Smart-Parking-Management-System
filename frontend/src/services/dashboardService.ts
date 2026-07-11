import { apiGet } from "./api";
import type { DashboardSummary, ParkingSession, Vehicle } from "../types/api";

export function fetchDashboardSummary() {
  return apiGet<DashboardSummary>("/dashboard/summary");
}

export function fetchActiveSessions() {
  return apiGet<ParkingSession[]>("/parking-sessions/active");
}

export function fetchHistory(limit = 10) {
  return apiGet<ParkingSession[]>("/parking-sessions/history", {
    query: { limit },
  });
}

export function fetchVehicles() {
  return apiGet<Vehicle[]>("/vehicles");
}

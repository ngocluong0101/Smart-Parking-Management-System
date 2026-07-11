import { Navigate, Route, Routes } from "react-router-dom";

import { AppLayout } from "./layouts/AppLayout";
import { DashboardPage } from "./pages/DashboardPage";
import { LoginPage } from "./pages/LoginPage";
import { VehiclePage } from "./pages/VehiclePage";
import { ParkingHistoryPage } from "./pages/ParkingHistoryPage";
import { StatisticsPage } from "./pages/StatisticsPage";
import { CameraLivePage } from "./pages/CameraLivePage";
import { SettingsPage } from "./pages/SettingsPage";
import { UserManagementPage } from "./pages/UserManagementPage";

export function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/" element={<AppLayout />}>
        <Route index element={<Navigate to="/dashboard" replace />} />
        <Route path="dashboard" element={<DashboardPage />} />
        <Route path="camera-live" element={<CameraLivePage />} />
        <Route path="vehicles" element={<VehiclePage />} />
        <Route path="history" element={<ParkingHistoryPage />} />
        <Route path="statistics" element={<StatisticsPage />} />
        <Route path="settings" element={<SettingsPage />} />
        <Route path="users" element={<UserManagementPage />} />
      </Route>
      <Route path="*" element={<Navigate to="/dashboard" replace />} />
    </Routes>
  );
}

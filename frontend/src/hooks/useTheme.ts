import { useEffect, useState } from "react";

export type ThemeMode = "dark" | "light";

const storageKey = "smart-parking-theme";

export function useTheme() {
  const [theme, setTheme] = useState<ThemeMode>(() => {
    const stored = window.localStorage.getItem(storageKey);
    return stored === "light" ? "light" : "dark";
  });

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    window.localStorage.setItem(storageKey, theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme((current) => (current === "dark" ? "light" : "dark"));
  };

  return { theme, toggleTheme };
}

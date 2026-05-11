import type { Config } from "tailwindcss";

export default {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./lib/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        // 따뜻한 다크 베이스
        surface: {
          DEFAULT: "#1a1b2e",
          card: "#222341",
          hover: "#2a2b4a",
          raised: "#2e2f52",
        },
        warm: {
          50:  "#fef9f0",
          100: "#fdf0dc",
          200: "#fbe0b8",
          300: "#f6c97c",
          400: "#f0a83e",
          500: "#e8901c",
          600: "#d07012",
          700: "#a85210",
          800: "#884214",
          900: "#703814",
        },
        // 포켓몬 타입 팔레트 (코딩 분류 매핑용)
        type: {
          fighting: "#C03028",
          psychic:  "#F85888",
          flying:   "#A890F0",
          steel:    "#B8B8D0",
          normal:   "#A8A878",
          grass:    "#78C850",
          fire:     "#F08030",
          water:    "#6890F0",
          ice:      "#98D8D8",
          dragon:   "#7038F8",
          rock:     "#B8A038",
          ghost:    "#705898",
          electric: "#F8D030",
          bug:      "#A8B820",
          poison:   "#A040A0",
          ground:   "#E0C068",
          dark:     "#705848",
          fairy:    "#EE99AC"
        }
      },
      fontFamily: {
        pixel: ["'Press Start 2P'", "monospace"],
        display: ["'Nunito'", "system-ui", "sans-serif"],
      },
      boxShadow: {
        card: "0 2px 8px rgba(0,0,0,0.2), 0 0 0 1px rgba(255,255,255,0.04)",
        "card-hover": "0 8px 24px rgba(0,0,0,0.3), 0 0 0 1px rgba(255,255,255,0.08)",
        glow: "0 0 20px rgba(248,208,48,0.15)",
        "glow-amber": "0 0 24px rgba(245,158,11,0.25)",
        "glow-emerald": "0 0 24px rgba(16,185,129,0.2)",
      },
      borderRadius: {
        "4xl": "2rem",
      },
      keyframes: {
        "float": {
          "0%, 100%": { transform: "translateY(0px)" },
          "50%":      { transform: "translateY(-12px)" },
        },
        "float-slow": {
          "0%, 100%": { transform: "translateY(0px)" },
          "50%":      { transform: "translateY(-8px)" },
        },
        "bounce-soft": {
          "0%, 100%": { transform: "translateY(0) scale(1)" },
          "50%":      { transform: "translateY(-4px) scale(1.02)" },
        },
        "fade-in": {
          from: { opacity: "0", transform: "translateY(8px)" },
          to:   { opacity: "1", transform: "translateY(0)" },
        },
        "slide-up": {
          from: { opacity: "0", transform: "translateY(20px)" },
          to:   { opacity: "1", transform: "translateY(0)" },
        },
        "wiggle": {
          "0%, 100%": { transform: "rotate(0deg)" },
          "25%":      { transform: "rotate(-3deg)" },
          "75%":      { transform: "rotate(3deg)" },
        },
        "sparkle": {
          "0%, 100%": { opacity: "1", transform: "scale(1)" },
          "50%":      { opacity: "0.6", transform: "scale(0.95)" },
        },
      },
      animation: {
        "float":       "float 3s ease-in-out infinite",
        "float-slow":  "float-slow 4s ease-in-out infinite",
        "bounce-soft": "bounce-soft 2s ease-in-out infinite",
        "fade-in":     "fade-in 0.4s ease-out",
        "slide-up":    "slide-up 0.5s ease-out",
        "wiggle":      "wiggle 1s ease-in-out infinite",
        "sparkle":     "sparkle 2s ease-in-out infinite",
      },
    }
  },
  plugins: []
} satisfies Config;

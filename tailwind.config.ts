import type { Config } from "tailwindcss";

export default {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}", "./lib/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        // 포켓몬 타입 팔레트 (코딩 분류 매핑용)
        type: {
          fighting: "#C03028",   // brute_force
          psychic:  "#F85888",   // dynamic_programming
          flying:   "#A890F0",   // graph_traversal
          steel:    "#B8B8D0",   // math
          normal:   "#A8A878",   // string
          grass:    "#78C850",   // tree / trie
          fire:     "#F08030",   // greedy
          water:    "#6890F0",   // simulation
          ice:      "#98D8D8",   // binary_search
          dragon:   "#7038F8",   // two_pointer
          rock:     "#B8A038",   // data_structure
          ghost:    "#705898",   // backtracking
          electric: "#F8D030",   // shortest_path
          bug:      "#A8B820",   // implementation
          poison:   "#A040A0",   // disjoint_set
          ground:   "#E0C068",   // prefix_sum
          dark:     "#705848",   // divide_and_conquer
          fairy:    "#EE99AC"    // minimum_spanning_tree
        }
      },
      fontFamily: {
        pixel: ["'Press Start 2P'", "monospace"]
      },
      boxShadow: {
        card: "0 6px 0 rgba(0,0,0,0.25), inset 0 -4px 0 rgba(0,0,0,0.15)"
      }
    }
  },
  plugins: []
} satisfies Config;

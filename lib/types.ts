export type Source = {
  lang: "python" | "cpp" | "java" | "javascript" | "typescript" | "kotlin" | "go" | "rust" | "c";
  file: string;
  code: string;
};

export type Problem = {
  id: string;
  slug: string;
  categorySlug: string;
  sources: Source[];
  link: string | null;
  authors: string[];
  hash: string;
  createdAt: number;
};

export type Category = {
  slug: string;
  name_ko: string;
  name_en: string;
  type: string;            // 포켓몬 타입 키 (tailwind colors.type.*)
  problemCount: number;
};

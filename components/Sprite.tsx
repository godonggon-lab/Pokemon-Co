"use client";

// 포켓몬 스프라이트 + 이미지 로드 실패 시 이모지 fallback.
// next/image 미사용 (외부 도메인) — 단순 <img>.

import { useState } from "react";

type Props = {
  src: string;
  alt: string;
  fallback: string;
  className?: string;
  size?: number;        // px
  silhouette?: boolean; // 미포획 표시
  pixelated?: boolean;
};

export default function Sprite({
  src, alt, fallback, className = "", size = 80, silhouette = false, pixelated = true
}: Props) {
  const [failed, setFailed] = useState(false);

  if (failed || !src) {
    return (
      <span
        className={`inline-flex items-center justify-center ${className}`}
        style={{ width: size, height: size, fontSize: size * 0.7 }}
        role="img" aria-label={alt}
      >
        {fallback}
      </span>
    );
  }

  return (
    <img
      src={src}
      alt={alt}
      width={size}
      height={size}
      loading="lazy"
      onError={() => setFailed(true)}
      className={`${pixelated ? "[image-rendering:pixelated]" : ""} ${
        silhouette ? "brightness-0 contrast-200 opacity-90" : ""
      } ${className}`}
    />
  );
}

# AI Reading Contract — CMN Template

Use this block at the top of files that will be read by an AI.

```txt
cmn1 prompt cmnReading rules
readMode semanticCompact
treatAs notes notCode
expandWhen needed
preserveMeaning y
askIf ambiguous y
reader aiPrimary humanSecondary
```

Explanatory note:

The AI must interpret CMN blocks as compact semantic notes. The notation must not be executed as code. When needed, the AI may expand the content into natural text while preserving the original meaning.

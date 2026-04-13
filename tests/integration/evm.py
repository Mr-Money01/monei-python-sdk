# Assert root fields
        assert result.statusCode is not None
        assert result.message is not None
        assert result.data is not None
        assert result.statusCode == 200

        # Extract typed portfolio
        p = result.data
        # === ASSERT ROOT PORTFOLIO FIELDS ===
        assert p.userId is not None
        assert p.walletAddress is not None
        assert p.network is not None
        assert p.totalPortfolioValueUSD is not None
        assert p.updatedAt is not None

        # === ASSERT NATIVE TOKEN ===
        native = p.nativeToken

        assert native.name is not None
        assert native.symbol is not None
        assert native.decimals is not None
        assert native.logoUrl is not None
        assert native.balance is not None
        assert native.balanceUSD is not None
        assert native.priceUSD is not None
        assert native.rawBalance is not None
        assert native.network is not None

        # === ASSERT TOKENS ARRAY ===
        tokens = p.tokens
        assert isinstance(tokens, list)

        if len(tokens) > 0:
            for t in tokens:
                assert isinstance(t.contractAddress, str)
                assert isinstance(t.name, str)
                assert isinstance(t.symbol, str)
                assert isinstance(t.decimals, int)
                assert isinstance(t.logoUrl, str)
                assert isinstance(t.type, str)
                assert isinstance(t.balance, str)
                assert isinstance(t.balanceUSD, str)
                assert isinstance(t.priceUSD, str)
                assert isinstance(t.rawBalance, str)
                assert isinstance(t.network, str)

        logger.info("Found %s tokens in portfolio.", len(tokens))
        logger.info("Checking first token: %s", tokens[0])






#SOLANA GET PORTFOLIO

 # === BASE RESPONSE ===
        assert "statusCode" in result
        assert "message" in result
        assert "data" in result

        p = result["data"]

        # === PORTFOLIO DATA ===
        assert "userId" in p
        assert "address" in p
        assert "nativeBalance" in p
        assert "nativeBalanceLamports" in p
        assert "tokens" in p

        # === VALIDATE NATIVE BALANCE TYPES ===
        assert isinstance(p["nativeBalance"], str)
        assert isinstance(p["nativeBalanceLamports"], str)

        # === TOKENS ARRAY ===
        assert isinstance(p["tokens"], list)

        if len(p["tokens"]) > 0:
            for t in p["tokens"]:
                # === MATCH OBJECT (like Jest toMatchObject) ===
                assert isinstance(t.get("mintAddress"), str)
                assert isinstance(t.get("name"), str)
                assert isinstance(t.get("symbol"), str)
                assert isinstance(t.get("balance"), (int, float))
                assert isinstance(t.get("rawBalance"), str)
                assert isinstance(t.get("decimals"), int)

        logger.info(
            "Sample Token Info: decimals=%s symbol=%s balance=%s mint=%s",
            t["decimals"],
            t["symbol"],
            t["balance"],
            t["mintAddress"],
        )

        logger.info(
            "Solana Portfolio Summary: %s",
            {
                "address": p.get("address"),
                "solBalance": p.get("nativeBalance"),
                "usdValue": p.get("totalValueUsd"),
                "tokenCount": len(p["tokens"]),
            },
        )

        
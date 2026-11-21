# Credit exchange between hotels

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: onet, auth, openhotel, web
- Discussion: none

## Summary
Friends are network-wide; furniture and credits stay in each hotel. Each hotel's credits become a currency that guests can swap on a network exchange, priced in OpenHotel credits (OHC). Mockup: [website-2001](website-2001/) `retro-exchange` and `retro-friends`.

## Motivation
Guests move between hotels but their credits don't. A fixed 1:1 rate would let one hotel print credits and drain the others, so the rate has to follow supply and demand.

## Proposal
- **Units**: every hotel has a credit code of 3 letters A-Z (OHC for the main hotel, PXP, NDK...), set when the hotel is created and never changed; codes are unique on the network. OHC is the quote currency; every pair is `XXX/OHC`.
- **Order book per pair**, run by onet: limit and market orders, matched by price then time. The exchange page lists hotel, credit, price and 24h only, plus your own exchange history; each credit has a page with a price chart, order book, supply and volume.
- **Settlement**: the seller's hotel burns the credits, the buyer's hotel mints the same value in its own credits. Both hotels sign the transfer with their licence, onet keeps the ledger.
- **Supply is public**: each hotel reports credits created and destroyed per day (signed). Printing too much lowers its own price, which is the brake.
- **Fees**: 1% per trade, paid in credits and burned. No real money anywhere: credits are only earned by playing.
- **Limits**: daily cap per account and per hotel; new accounts and new hotels start lower. Trading pauses for a hotel whose reports stop or don't add up.
- **Furniture never moves**; only credits.
- **Opt-in**: a hotel joins the exchange from My hotels. Private hotels can't list.

## Alternatives
| Option | For | Against |
|---|---|---|
| Fixed rates set by OpenHotel | Simple | Doesn't follow supply; manual work |
| Order book (proposed) | Fair prices, familiar | Needs liquidity on small hotels |
| Pool per pair (automatic market maker) | Always liquid | Hotels must lock credits; harder to explain |

## Impact
- onet: order book, matching, ledger, daily supply reports, limits.
- openhotel (server): mint/burn endpoints signed with the licence; supply counters.
- auth: per-account limits and account age.
- web: exchange page, wallets per hotel; friends page reads auth.

## Open questions
1. Start with a fixed-rate pilot between two hotels before the order book?
2. Who seeds liquidity on a new pair: the hotel owner, or nobody?
3. What happens to open orders when a hotel goes offline for days?
4. Should OHC have a cap so the main hotel can't inflate the quote currency?

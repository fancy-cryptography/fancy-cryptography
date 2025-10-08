# Fancy cryptography in the wild 🎩

Curated list of deployments of *fancy* cryptography.

Cryptography counts as fancy if it uses primitives beyond symmetric ciphers,
(EC)DH as key agreement, digital signatures, public key encryption such as
RSA-OAEP, or KEMs, or uses those
primitives in unusual ways, especially if it relies on properties beyond IND-CCA2.

A secondary goal of this list is to provide cryptographers with a list
of schemes that still need to be upgraded to post-quantum cryptography.

💫  [Contributions welcome](https://github.com/fancy-cryptography/fancy-cryptography/edit/main/README.md)

## Large-scale mainstream deployments

* **Android Nearby Share/Quick Share.**  
  PAKE and various weird stuff  
  Reading: TBD.  
  Fully PQ: 😔.

* **Apple Homekit device enrollment**  
  aPAKE (SRP / SPAKE2+ (Matter))  
  Reading: [documentation](https://support.apple.com/nl-nl/guide/security/sec3a881ccb1/web).  
  Fully PQ: 😔.

* **Apple Keychain key escrow**  
  aPAKE (SRP), threshold cryptography? ("majority of HSMs agrees").  
  Reading: [documentation](https://support.apple.com/nl-nl/guide/security/sec3e341e75d/web).  
  Fully PQ: 😔.

* **Apple Carkey**  
  aPAKE (SPAKE2+).  
  Reading: [documentation](https://support.apple.com/nl-nl/guide/security/secf64471c16/web).  
  Fully PQ: 😔.

* **Apple Private Relay.**  
  Blind signatures for anonymous tokens.  
  Reading: [overview](https://www.apple.com/icloud/docs/iCloud_Private_Relay_Overview_Dec2021.pdf).  
  Fully PQ: 😔.

* **Apple Private Cloud Compute.**  
  Blind signatures for anonymous tokens.  
  Reading: [blog](https://security.apple.com/blog/private-cloud-compute/).  
  Fully PQ: 😔.

* **Apple/Google Exposure Notifications.**  
  Bespoke protocol.  
  Reading: [overview (archive.org)](https://web.archive.org/web/20240709100147/https://www.google.com/covid19/exposurenotifications/).  
  Fully PQ: 😊 (with the exception of some signatures which could easily be changed to ML-DSA).

* **Apple Live Caller ID lookup.**  
  PIR using FHE.  
  Reading: [blog](https://www.swift.org/blog/announcing-swift-homomorphic-encryption/)  
  Fully PQ: 😊 (with the exception of anonymous tokens used for rate-limiting)

* **Chrome compromised passwords check.**  
  Private Set Intersection.  
  Reading: [blog](https://security.googleblog.com/2019/12/better-password-protections-in-chrome.html).  
  Fully PQ: 😔.

* **Cloudflare Geo Key Manager.**  
  Attribute/Identity-based encryption.  
  Reading: [blog](https://blog.cloudflare.com/inside-geo-key-manager-v2/).  
  Fully PQ: 😔.

* **1Password user authentication.**  
  aPAKE (SRP)  
  Reading: [blog](https://blog.1password.com/developers-how-we-use-srp-and-you-can-too/).  
  Fully PQ: 😔.

* **Mozilla Firefox telemetry.**  
  Oblivious HTTP, Prio privacy-preserving statistics.  
  Reading: [blog](https://blog.mozilla.org/en/products/firefox/partnership-ohttp-prio/),
           [prio paper](https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/corrigan-gibbs),
           [OHTTP spec](https://datatracker.ietf.org/doc/html/rfc9458),
           [Distributed Aggregation Protocol spec](https://datatracker.ietf.org/doc/draft-ietf-ppm-dap/).  
  Fully PQ: 😔 (if PQ configurations of TLS and HPKE are used).

* **Matter device enrollment**  
  aPAKE (SPAKE2+)  
  Reading: [documentation](https://docs.silabs.com/matter/2.2.0/matter-fundamentals-security/)  
  Fully PQ: 😔

* **Passport chip access control**  
  PAKE (PACE)  
  Reading: [overview](https://www.icao.int/Security/FAL/PKD/BVRT/Pages/Document-readers.aspx), [spec](https://www.icao.int/publications/documents/9303_p10_cons_en.pdf).  
  Fully PQ: 😔.

* **Facebook Messenger chat history sharing**  
  PAKE (CPace)  
  Reading: [Labyrinth](https://engineering.fb.com/wp-content/uploads/2023/12/TheLabyrinthEncryptedMessageStorageProtocol_12-6-2023.pdf) (p35)  
  Fully PQ: 😔.

* **Signal private group system.**  
  Key-verification anonymous credentials.  
  Reading: [blog](https://signal.org/blog/signal-private-group-system/).  
  Fully PQ: 😔.

* **WhatsApp encrypted backups.**  
  aPAKE (OPAQUE) for backup key retrieval from PIN.  
  Reading: [presentation](https://iacr.org/submit/files/slides/2023/rwc/rwc2023/IT_2/slides.pdf),
           [Meta whitepaper](https://scontent-lhr8-1.xx.fbcdn.net/v/t39.8562-6/241394876_546674233234181_8907137889500301879_n.pdf?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=W2f98GDJW1MQ7kNvgEi9dJ0&_nc_ht=scontent-lhr8-1.xx&oh=00_AYC2S2KAHkBXa60RvLU1sOfP5Y_rCNgj_LOzHpSZ7RwStw&oe=666E0A26),
            [Academic paper](https://eprint.iacr.org/2023/843),
           [audit](https://research.nccgroup.com/wp-content/uploads/2021/10/NCC_Group_WhatsApp_E001000M_Report_2021-10-27_v1.2.pdf).  
  Fully PQ: 😔.

* **Signal encrypted backups.**  
  Password-protected Secret Sharing (PPSS) based on OPRF for key retreival from PIN.  
  Reading: [Academic paper](https://eprint.iacr.org/2024/887.pdf),
           [Code](https://github.com/signalapp/SecureValueRecovery2)  
  Fully PQ: 😔.

* **league of entropy (drand).**
  Public verifiable decentralised randomness using threshold signatures and distributed key generation.  
  Reading: [website](https://www.drand.love/loe), [docs](https://docs.drand.love/about/)
  Fully PQ: 😔.

* (...)

## Web3 / Blockchain

* **Zcash shielded transactions.**  
  zk-SNARKs, homomorphic Pedersen commitments, re-randomizable signing keys, key-private public-key encryption (see Post-Quantum Zcash presentation below for more detail).  
  Reading: [security analysis (with PQ notes)](https://github.com/daira/zcash-security),
           [circuit statements](https://zips.z.cash/protocol/protocol.pdf#snarkstatements),
           [Groth16 (trusted setup)](https://eprint.iacr.org/2016/260),
           [Halo2 (trustless)](https://zcash.github.io/halo2/design/protocol.html),
           [commitment specs](https://zips.z.cash/protocol/protocol.pdf#concretehomomorphiccommit),
           [RedDSA](https://zips.z.cash/protocol/protocol.pdf#concretereddsa).<br>
  Fully PQ: 😔. Has PQ privacy when the adversary doesn't know the recipient's address; no PQ correctness.<br>
  Future proposals:
  * Post-Quantum Zcash presentation: [slides](https://docs.google.com/presentation/d/1BHBiSOEO5zt40KWBbRXVMGIIuAcT2hfPWZQ3pT_8tm8/edit), [video](https://www.youtube.com/watch?v=T2B5f297d-Y)<br>
  * [Proposal for "quantum resilience" (draft)](https://hackmd.io/fF6D7THmRDamvyAAsJN5yw?view): "This ZIP proposes a change to the construction of Orchard notes that is intended to support a smoother transition to future versions of Zcash designed to be secure against discrete-log-breaking adversaries, including adversaries using quantum computers."

* (...)
  
## Proofs of Concept / Growing / Niche

* **Facebook secure update propagation.**  
  Homomorphic hashing (aka incremental hashing)  
  Reading:  [blog](https://engineering.fb.com/2019/03/01/security/homomorphic-hashing/), [code](https://github.com/facebook/folly/blob/main/folly/crypto/LtHash.cpp).  
  Fully PQ:  🤨 potentially with a PQ-signature scheme signing homomorphic hashes

* **Facebook ads attribution.**  
  Private match and compute  
  Reading: [blog 1](https://engineering.fb.com/2020/07/10/open-source/private-matching/), [blog 2](https://research.facebook.com/blog/2023/1/delegated-multi-key-private-matching-for-compute-improving-match-rates-and-enabling-adoption/), [code](https://github.com/facebookresearch/Private-ID).  
  Fully PQ: 😔.

* **Google ads attribution.**  
  Private join and compute
  Reading: [blog](https://security.googleblog.com/2019/06/helping-organizations-do-more-without-collecting-more-data.html), [code](https://github.com/google/private-join-and-compute).  
  Fully PQ: 😔.

* **Google ads attribution.**  
  Partially homomorphic encryption for private set intersection using Paillier  
  Reading:  [blog](https://bristolcrypto.blogspot.com/2017/01/rwc-2017-secure-mpc-at-google.html), [Media coverage](https://www.theverge.com/2018/8/30/17801880/google-mastercard-data-online-ads-offline-purchase-history-privacy), [patent](https://research.google/pubs/private-intersection-sum-protocols-with-applications-to-attributing-aggregate-ad-conversions/).  
  Fully PQ:  😔. Paillier is not post-quantum secure.
 
* **IACR voting**
  Mixnets  
  Reading:  [Helios](https://www.usenix.org/legacy/events/sec08/tech/full_papers/adida/adida.pdf).  
  Fully PQ:  TBD.

* (...)

## See also

* [MPC Deployments](https://mpc.cs.berkeley.edu/)
* [IETF PQUIP working group's "state of protocols and PQC"](https://github.com/ietf-wg-pquip/state-of-protocols-and-pqc)
* [UK National Cyber Security Centre "Advanced Cryptography" whitepaper](https://www.ncsc.gov.uk/whitepaper/advanced-cryptography)

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

* **Signal private group system.**  
  Key-verification anonymous credentials.  
  Reading: [blog](https://signal.org/blog/signal-private-group-system/).
  Fully PQ: 😔.

* **Apple Homekit device enrollment**  
  PAKE (SRP).  
  Reading: [documentation](https://support.apple.com/nl-nl/guide/security/sec3a881ccb1/web).
	Fully PQ: 😔.

* **Apple Keychain key escrow**  
  PAKE (SRP), threshold cryptography? ("majority of HSMs agrees").  
  Reading: [documentation](https://support.apple.com/nl-nl/guide/security/sec3e341e75d/web).
  Fully PQ: 😔.

* **Apple Carkey**  
  PAKE (SPAKE2+).  
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
  Reading: [overview](https://www.google.com/covid19/exposurenotifications/).  
  Fully PQ: 😊 (with the exception of some signatures which could easily be changed to ML-DSA).

* **WhatsApp encrypted backups.**  
  OPAQUE for backup key retrieval from PIN.  
  Reading: [presentation](https://iacr.org/submit/files/slides/2023/rwc/rwc2023/IT_2/slides.pdf),
           [Meta whitepaper](https://scontent-lhr8-1.xx.fbcdn.net/v/t39.8562-6/241394876_546674233234181_8907137889500301879_n.pdf?_nc_cat=108&ccb=1-7&_nc_sid=e280be&_nc_ohc=W2f98GDJW1MQ7kNvgEi9dJ0&_nc_ht=scontent-lhr8-1.xx&oh=00_AYC2S2KAHkBXa60RvLU1sOfP5Y_rCNgj_LOzHpSZ7RwStw&oe=666E0A26),
            [Academic paper](https://eprint.iacr.org/2023/843),
           [audit](https://research.nccgroup.com/wp-content/uploads/2021/10/NCC_Group_WhatsApp_E001000M_Report_2021-10-27_v1.2.pdf).
  Fully PQ: 😔.

* **Chrome compromised passwords check.**  
  Private Set Intersection.  
  Reading: [blog](https://security.googleblog.com/2019/12/better-password-protections-in-chrome.html).
  Fully PQ: 😔.

* **Android Nearby Share/Quick Share.**  
  PAKE and various weird stuff  
  Reading: tbd  
  Fully PQ: 😔.

* **Cloudflare Geo Key Manager.**  
  Attribute/Identity-based encryption.  
  Reading: [blog](https://blog.cloudflare.com/inside-geo-key-manager-v2/).
  Fully PQ: 😔.

* **Passport chip access control**
  PAKE (PACE)
  Reading: [overview](https://www.icao.int/Security/FAL/PKD/BVRT/Pages/Document-readers.aspx), [spec](https://www.icao.int/publications/documents/9303_p10_cons_en.pdf)
  
* (...)

## Web3 / Blockchain

* **Zcash shielded transactions.**  
  zk-SNARKs, homomorphic Pedersen commitments, re-randomizable signing keys.  
  Reading: [security analysis (with PQ notes)](https://github.com/daira/zcash-security),
           [circuit statements](https://zips.z.cash/protocol/protocol.pdf#snarkstatements),
           [Groth16 (trusted setup)](https://eprint.iacr.org/2016/260),
           [Halo2 (trustless)](https://zcash.github.io/halo2/design/protocol.html),
           [commitment specs](https://zips.z.cash/protocol/protocol.pdf#concretehomomorphiccommit),
           [RedDSA](https://zips.z.cash/protocol/protocol.pdf#concretereddsa).  
  Fully PQ: 😔. Has PQ privacy when the adversary doesn't know the recipient's address; no PQ correctness.

* (...)
  
## Growing or niche

* **IACR voting**  
  Reading:  [Helios](https://www.usenix.org/legacy/events/sec08/tech/full_papers/adida/adida.pdf).
  Fully PQ: TBD.

* (...)

## See also

* [IETF PQUIP working group's "state of protocols and PQC"](https://github.com/ietf-wg-pquip/state-of-protocols-and-pqc)

# Credit Card Customer Segmentation — Summary Report

## 1. Business problem and dataset
A large Indian private bank wants to replace one-size-fits-all card offers with behavioural segments so Relationship Managers can give the right product to the right customer, reducing attrition and raising wallet share. The data is the Kaggle credit-card clustering dataset: 8,950 active cardholders and 17 behavioural and financial columns (balance, purchases, cash advance, credit limit, payments, tenure and frequencies). `CUST_ID` was dropped; 0 missing CREDIT_LIMIT and 0 missing MINIMUM_PAYMENTS values were imputed with the median. 22.8% of customers never made a purchase, and the top 26% of customers generate 80% of purchase volume.

## 2. Feature engineering and preprocessing
Four behavioural features were added: Monthly_Avg_Purchase, Monthly_Avg_Cash_Advance, Limit_Usage (balance / limit) and Payment_to_Minpayment_Ratio. Money columns are heavily right-skewed with extreme values, so outliers were winsorised at Q3 + 3×IQR (no rows dropped) and log1p-transformed, then standardised, because K-Means, hierarchical clustering and DBSCAN are all distance-based and scale-sensitive.

## 3. Algorithm comparison
| Algorithm | Settings | Clusters | Silhouette | Davies-Bouldin | Calinski-Harabasz | Noise % |
|---|---|---|---|---|---|---|
| K-Means | k=3, init=k-means++, n_init=20 | 3 | 0.223 | 1.679 | 2,729 | 0.0 |
| Agglomerative | n_clusters=3, linkage=ward | 3 | 0.198 | 1.728 | 2,213 | 0.0 |
| DBSCAN | eps=2.03, min_samples=10 | 3 | 0.122 | 0.951 | 87 | 8.3 |

K-Means ranks first on the combined metric ranking; **K-Means** is the recommended model for deployment because it covers all customers with 3 actionable segments and is stable across seeds (silhouette std 0.000). Hierarchical and K-Means agreement (ARI) is 0.33. DBSCAN flags 8.3% of customers as noise — unusual accounts best handled by manual review.

## 4. Segments
- **Premium Spenders** (36%): balance 1.3x, purchases 2.2x, cash advance 0.8x, credit limit 1.2x, full-payment share 0.9x the portfolio average.
- **Cash-Advance Reliant** (32%): balance 1.5x, purchases 0.1x, cash advance 2.2x, credit limit 0.9x, full-payment share 0.2x the portfolio average.
- **Low-Balance Full Payers** (32%): balance 0.1x, purchases 0.6x, cash advance 0.0x, credit limit 0.8x, full-payment share 1.9x the portfolio average.

## 5. Business actions
- Premium Spenders: Upgrade to a premium/super-premium card with travel and lifestyle rewards and a higher limit.
- Cash-Advance Reliant: Offer a low-rate personal loan or cash-advance-to-EMI conversion; monitor credit risk.
- Low-Balance Full Payers: Drive spend with cashback/EMI-on-card offers and merchant tie-ups; they are low-risk and under-used.

## 6. Next steps
Add transaction-level and time-series features (spend trends, merchant categories), delinquency and churn labels for semi-supervised refinement, and serve the saved scaler and model behind a real-time scoring API (a Streamlit prototype, `app.py`, is included).

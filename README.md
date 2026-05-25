# MSX 邮件模板

MSX 业务邮件 HTML 模板仓库，按语言与版本分目录存放，供后端渲染后发送。

## 目录结构

```
mail/
├── README.md                          # 本文件
├── _batch_inline_all.py               # 批量内联样式脚本
├── empty_template.html                # 空白模板（中文，含页头）
├── empty_template_en.html             # 空白模板（英文，含页头）
├── empty_template_nohead.html         # 空白模板（中文，无页头）
├── empty_template_nohead_en.html      # 空白模板（英文，无页头）
├── verification_code_zh.html          # 验证码（中文，Go 模板）
├── verification_code_en.html          # 验证码（英文，Go 模板）
├── new_zh/                            # 新版模板（中文）
├── new_en/                            # 新版模板（英文）
├── zh/                                # 旧版模板（中文）
├── en/                                # 旧版模板（英文）
└── trade/                             # 交易相关 / 样式参考模板
```

## 模板索引

### 基础模板

| 文件 | 说明 |
| --- | --- |
| [empty_template.html](empty_template.html) | 空白模板（中文） |
| [empty_template_en.html](empty_template_en.html) | 空白模板（英文） |
| [empty_template_nohead.html](empty_template_nohead.html) | 空白模板（中文，无页头） |
| [empty_template_nohead_en.html](empty_template_nohead_en.html) | 空白模板（英文，无页头） |
| [verification_code_zh.html](verification_code_zh.html) | 验证码（中文） |
| [verification_code_en.html](verification_code_en.html) | 验证码（英文） |

### 新版模板 `new_zh/` / `new_en/`

| 中文 | 英文 | 模板参数 |
| --- | --- | --- |
| [ipo_confirmation_expired_shares.html](new_zh/ipo_confirmation_expired_shares.html) | [ipo_confirmation_expired_shares.html](new_en/ipo_confirmation_expired_shares.html) | `${projectName1}` `${subscriptionAmount1}` `${confirmedAmount1}` `${confirmedPrice1}` `${refundAmount1}` `${projectName2}` `${subscriptionAmount2}` `${confirmedAmount2}` `${confirmedPrice2}` `${refundAmount2}` |
| [ipo_subscription_due_settlement_notice.html](new_zh/ipo_subscription_due_settlement_notice.html) | [ipo_subscription_due_settlement_notice.html](new_en/ipo_subscription_due_settlement_notice.html) | `${accountEmail}` `${ipoName}` `${subscriptionToken}` `${purchaseAmount}` `${issuePrice}` `${distributedQuantity}` |
| [register_success_msg.html](new_zh/register_success_msg.html) | [register_success_msg.html](new_en/register_success_msg.html) | — |
| [2fa-setup_successful.html](new_zh/2fa-setup_successful.html) | [2fa-setup_successful.html](new_en/2fa-setup_successful.html) | `${updatedAt}` |
| [kyc_authentication_results.html](new_zh/kyc_authentication_results.html) | [kyc_authentication_results.html](new_en/kyc_authentication_results.html) | `${userId}` `${familyName}` `${name}` `${status}` `${auditTime}` |
| [ip_login_alert_msg.html](new_zh/ip_login_alert_msg.html) | [ip_login_alert_msg.html](new_en/ip_login_alert_msg.html) | `${email}` `${loginAt}` `${ip}` `${location}` |
| [spot_order_fully_filled.html](new_zh/spot_order_fully_filled.html) | [spot_order_fully_filled.html](new_en/spot_order_fully_filled.html) | `${symbol}` `${filledAt}` `${filledQuantity}` `${avgPrice}` |
| [stop_profit_loss_msg.html](new_zh/stop_profit_loss_msg.html) | [stop_profit_loss_msg.html](new_en/stop_profit_loss_msg.html) | `${email}` `${symbol}` `${orderType}` `${triggerPrice}` `${executedPrice}` `${filledQuantity}` `${executedAt}` |
| [dividend_msg.html](new_zh/dividend_msg.html) | [dividend_msg.html](new_en/dividend_msg.html) | `${symbol}` `${amount}` `${coin}` `${account}` `${distributedAt}` `${shares}` `${dividendPerShare}` |
| [multiple_currency_liquidation_reminder.html](new_zh/multiple_currency_liquidation_reminder.html) | [multiple_currency_liquidation_reminder.html](new_en/multiple_currency_liquidation_reminder.html) | `${email}` `${marginRatio}` `${warningThreshold}` `${maintenanceMargin}` `${symbol1}` `${leverage1}` `${direction1}` `${directionColor1}` `${quantity1}` `${markPrice1}` `${estLiqPrice1}` `${unrealizedPnl1}` `${symbol2}` `${leverage2}` `${direction2}` `${directionColor2}` `${quantity2}` `${markPrice2}` `${estLiqPrice2}` `${unrealizedPnl2}` |
| [multiple_currencies_have_been_liquidated.html](new_zh/multiple_currencies_have_been_liquidated.html) | [multiple_currencies_have_been_liquidated.html](new_en/multiple_currencies_have_been_liquidated.html) | `${email}` `${symbol1}` `${leverage1}` `${direction1}` `${directionColor1}` `${quantity1}` `${markPrice1}` `${liquidationTime1}` `${symbol2}` `${leverage2}` `${direction2}` `${directionColor2}` `${quantity2}` `${markPrice2}` `${liquidationTime2}` |

### 旧版模板 `zh/` / `en/`

| 中文 | 英文 | 模板参数 |
| --- | --- | --- |
| [verification_code_zh.html](zh/verification_code_zh.html) | [verification_code_en.html](en/verification_code_en.html) | `${number}` |
| [deposit_success_msg.html](zh/deposit_success_msg.html) | [deposit_success_msg.html](en/deposit_success_msg.html) | `${amount}` `${coin}` `${network}` `${walletAddress}` `${txHash}` `${createdAt}` |
| [withdraw_success_msg.html](zh/withdraw_success_msg.html) | [withdraw_success_msg.html](en/withdraw_success_msg.html) | `${actualAmount}` `${coin}` `${network}` `${addressTo}` `${txHash}` `${createdAt}` |
| [withdraw_fail_msg.html](zh/withdraw_fail_msg.html) | [withdraw_fail_msg.html](en/withdraw_fail_msg.html) | — |
| [liquidation_msg.html](zh/liquidation_msg.html) | [liquidation_msg.html](en/liquidation_msg.html) | `${symbol}` `${side}` `${posType}` `${qty}` `${posMargin}` `${liqPrice}` `${maintenanceMarginRate}` `${bankruptcyPrice}` `${markPrice}` `${triggerTime}` |
| [gt_success_msg.html](zh/gt_success_msg.html) | [gt_success_msg.html](en/gt_success_msg.html) | — |
| [gt_fail_msg.html](zh/gt_fail_msg.html) | [gt_fail_msg.html](en/gt_fail_msg.html) | — |
| [xcard_activation_code.html](zh/xcard_activation_code.html) | [xcard_activation_code.html](en/xcard_activation_code.html) | `${card_number}` `${number}` |
| [xcard_activate_success_msg.html](zh/xcard_activate_success_msg.html) | [xcard_activate_success_msg.html](en/xcard_activate_success_msg.html) | — |
| [xcard_activate_fail_msg.html](zh/xcard_activate_fail_msg.html) | [xcard_activate_fail_msg.html](en/xcard_activate_fail_msg.html) | — |
| [xcard_bind_card_success_msg.html](zh/xcard_bind_card_success_msg.html) | [xcard_bind_card_success_msg.html](en/xcard_bind_card_success_msg.html) | — |
| [xcard_bind_card_fail_msg.html](zh/xcard_bind_card_fail_msg.html) | [xcard_bind_card_fail_msg.html](en/xcard_bind_card_fail_msg.html) | — |
| [xcard_created_holder_success.html](zh/xcard_created_holder_success.html) | [xcard_created_holder_success.html](en/xcard_created_holder_success.html) | — |
| [xcard_created_holder_failed.html](zh/xcard_created_holder_failed.html) | [xcard_created_holder_failed.html](en/xcard_created_holder_failed.html) | — |
| [xcard_recharge_success_msg.html](zh/xcard_recharge_success_msg.html) | [xcard_recharge_success_msg.html](en/xcard_recharge_success_msg.html) | — |
| [xcard_recharge_fail_msg.html](zh/xcard_recharge_fail_msg.html) | [xcard_recharge_fail_msg.html](en/xcard_recharge_fail_msg.html) | — |
| [xcard_withdraw_success_msg.html](zh/xcard_withdraw_success_msg.html) | [xcard_withdraw_success_msg.html](en/xcard_withdraw_success_msg.html) | — |
| [xcard_withdraw_fail_msg.html](zh/xcard_withdraw_fail_msg.html) | [xcard_withdraw_fail_msg.html](en/xcard_withdraw_fail_msg.html) | — |

### 交易目录 `trade/`

| 文件 | 说明 |
| --- | --- |
| [withdraw_success_zh.html](trade/withdraw_success_zh.html) | 样式参考模板，供 `_batch_inline_all.py` 批量处理时使用 |

## 模板参数说明

- 各 HTML 文件 `<head>` 内通常有 `<!-- template params: ... -->` 注释，列出该模板所需的占位变量。
- 变量格式为 `${variableName}`，部分模板（如验证码）使用 Go 模板语法 `{{.FieldName}}`。
- 无参数需求的模板在注释中标注为 `(none)` 或表格中以 `—` 表示。

## 工具脚本

```bash
python3 _batch_inline_all.py
```

该脚本会基于 `trade/withdraw_success_zh.html` 的外壳，批量处理邮件模板：移除 `<style>`、内联样式，并做邮件客户端兼容性修正。

<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                        >
                            <td>{{ item.product.name }}</td>
                            <td>${{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Address*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>

                        <div class="field">
                            <label>Zip code*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode">
                            </div>
                        </div>

                        <div class="field">
                            <label>Place*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div class="column is-12 box">
                <div id="card-element" class="mb-5">
                    <!-- Simulate card input fields (for demonstration purposes) -->
                    <label for="card-number">Card Number</label>
                    <input type="text" id="card-number" class="input">
                    <label for="card-expiration">Expiration Date</label>
                    <input type="text" id="card-expiration" class="input">
                    <label for="card-cvv">CVV</label>
                    <input type="text" id="card-cvv" class="input">
                </div>

                <template v-if="cartTotalLength">
                    <hr>
                    <button class="button is-dark" @click="simulatePayment">Pay with Stripe</button>
                </template>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Checkout',
  data() {
    return {
      cart: {
        items: []
      },
      first_name: '',
      last_name: '',
      email: '',
      phone: '',
      address: '',
      zipcode: '',
      place: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Checkout | Djackets'
    this.cart = this.$store.state.cart
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    simulatePayment() {
      // Simulate a successful payment
      setTimeout(() => {
        // Clear the cart (simulated)
        this.$store.commit('clearCart')

        // Redirect to the success page
        this.$router.push('/cart/success')
      }, 2000); // Simulate a 2-second delay (replace with actual logic)
    },
  },
  computed: {
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.product.price * curVal.quantity
      }, 0)
    },
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0)
    }
  }
}
</script>

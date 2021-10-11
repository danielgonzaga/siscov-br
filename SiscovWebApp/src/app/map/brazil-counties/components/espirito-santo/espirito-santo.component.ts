import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-espirito-santo',
  templateUrl: './espirito-santo.component.html',
  styleUrls: ['./espirito-santo.component.css']
})
export class EspiritoSantoComponent implements OnInit {

  @Output() clickedLocal = new EventEmitter;

  constructor() { }

  ngOnInit(): void {}

  getLocal(event) {
    this.clickedLocal.emit(event);
  }

}

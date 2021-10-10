import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AmapaComponent } from './amapa.component';

describe('AmapaComponent', () => {
  let component: AmapaComponent;
  let fixture: ComponentFixture<AmapaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AmapaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AmapaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
